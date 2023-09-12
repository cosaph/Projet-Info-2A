# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    API_recherche_de_stage.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/12 09:05:52 by cosaph            #+#    #+#              #
#    Updated: 2023/09/12 09:15:23 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({'hello': 'world'})


app = Starlette(debug=True, routes=[
    Route('/', homepage),
])