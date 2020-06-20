import asyncio
import pandas as pd
import random


async def add(row):
    print(row)
    while True:
        global df
        if not row in df.index:
            df = df.append(pd.DataFrame({'wert':row, 'value':  random.randint(0, 10)}, index=[row]))
        else:
            df.update(pd.DataFrame({'wert':row, 'value':  random.randint(0, 10)}, index=[row]))
        print(df)
        await asyncio.sleep(1)

df=pd.DataFrame(columns=['wert'])

async def main():
    await asyncio.gather(add( 'eins'), add('zwei'))

if __name__ == "__main__":
    asyncio.run(main())

#loop = asyncio.get_event_loop()
#loop.run_until_complete(add(df, 1))
#loop.run_until_complete(add(df, 2))
#print(df)
#loop.close()
