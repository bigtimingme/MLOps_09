from fastapi import FastAPI
import pandas as pd

app = FastAPI()
app.setup()

total_df = pd.read_csv('df_fastapi.csv')

@app.get('/')
async def root():
    return {'Proyecto Individual de SOY HENRY del alumno Francisco Jimenez de Arechaga'}

@app.get('/get_max_duration/{year}/{plat}/{dur_type}')
async def get_max_duration(year:int=None,plat:str=None,dur_type:str='min'):

    mytitle = total_df[(total_df['release_year']==year) & (total_df['platform']==plat) & (total_df['type']=='movie') &
                       (total_df['duration_type']==dur_type)]
    maxi = mytitle[mytitle['duration_int'] == max(mytitle['duration_int'])][['title','duration_int']]
    title = maxi.iloc[0].values[0]
    duration = maxi.iloc[0].values[1]
        
    return {'title':title,'duration':duration,'duration_type':dur_type}

@app.get('/get_score_count/{platform}/{scored}/{year}')
async def get_score_count(platform:str,scored:float,year:int):
    a = int(total_df[(total_df['platform']==platform)&(total_df['scored']>scored)&(total_df['release_year']==year)]['title'].count())
    return {f'cantidad de contents arriba de {scored} puntos': a}

@app.get('/get_count_platform/{platform}')
def get_count_platform(platform:str):
    a = int(total_df[(total_df['platform']==platform) & (total_df['type']=='movie')]['title'].count())
    return {f'cantidad de contents en {platform}':a}

@app.get('/get_actor/{platform}/{year}')
def get_actor(platform:str,year:int):
    if platform=='hulu':
        return {'data no disponible para Hulu'}
    else:
        a = total_df[(total_df['platform']==platform)&(total_df['release_year']==year)]['cast']
        actorslist = []
        for i in a:
            if type(i) == str:
                b = i.split(',')
                for i in b:
                    if i.startswith(' '):
                        actorslist.append(i[1:])
                    else:
                        actorslist.append(i)
            else:
                pass

    a = actorslist
    counter = 0
    num = a[0]
    for i in a:
        curr_frequency = a.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
    return {'actor':num,'cantidad de veces':a.count(num)}


@app.get('/prod_per_country')
async def products_per_country(country:str,year:int,content:str):
    a = len(total_df[(total_df['country']== country) & (total_df['release_year']== year) & (total_df['type']==content)])
    return {f'cantidad de películas de {country} en el year {year} del tipo {content} es: {a}'}

@app.get('/get_contents')
async def get_contents(rating:float):
    contenido = len(total_df[total_df['scored'] == rating])
    return {f'Cantidad de contenido con puntaje {rating} es: {contenido}'}

@app.get('/recommender')
async def recommender(movie):
    a = total_df[total_df['title']==movie]['recommender']
    recommender = [i for i in a]
    return {f'contents recomendadas para {movie} son: {recommender}'}