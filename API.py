# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    API.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/05 19:29:18 by cosaph            #+#    #+#              #
#    Updated: 2023/09/09 22:14:07 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



query_input = input("Enter what type of internship you want: ")
location_input = input("In which location? ")
country_input = input("In which country? ")
radius_input = input("Dans un rayon de combien de km? ")

querystring = {
    "q": query_input,
    "page": "1",
    "country": country_input,
    "city": location_input,
    "radius": radius_input,
    "fromage": "20"
}


import requests

url = "https://workable.p.rapidapi.com/%7BAPIKEY%7D/jobs"


headers = {
	"X-RapidAPI-Key": "999df5a4d0mshf48fb1f93f36f8dp18ac14jsn6868c02acc03",
	"X-RapidAPI-Host": "workable.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())