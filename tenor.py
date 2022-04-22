import asyncio
from pytenor import Tenor

api = Tenor(key="N5WQ3J0VMWM9")


async def main():
    # Search for gifs. This returns a GIF object.
    gifs = await api.search()

    print("Here are the gifs I found")
    for gif in gifs:
        print(f"{gif.url}")


if __name__ == "__main__":
    asyncio.run(main())