import aiohttp
import asyncio

url = 'ur website, like a webhook or github page.'

num_views = 100

async def make_request(session, url, i):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                print(f"Visualização {i + 1} realizada com sucesso.")
            else:
                print(f"Falha na visualização {i + 1}. Status code: {response.status}")
    except Exception as e:
        print(f"Erro na visualização {i + 1}: {str(e)}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(num_views):
            task = make_request(session, url, i)
            tasks.append(task)
        
        # Executar todas as requisições de forma assíncrona
        await asyncio.gather(*tasks)

asyncio.run(main())
