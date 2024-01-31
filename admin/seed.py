import asyncio

from app_admin.mongoengine.seed import fill_database as fill_mongo_database


async def main():
    print("Start filling MongoEngine database")
    await fill_mongo_database()
    print("End filling MongoEngine database")


asyncio.run(main())
