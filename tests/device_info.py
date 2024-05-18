import paypy
import asyncio


async def main() -> None:
    client = paypy.BaseClient()
    device_info = await client._construct_device_info()
    print(device_info)


if __name__ == "__main__":
    asyncio.run(main())
