import asyncio
from pyrogram import Client


async def main():
    print("- Jmthon Session Pyrogram -")
    print("\n---------------------------\n")
    api_id = int(input("15192591"))
    api_hash = input("30685a4416b114f1b91921c7b30ca74a")
    print("\n---------------------------\n")
    async with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
        await app.send_message(
            "me",
            "**كود سيشن البايروجرام**:\n\n"
            f"`{await app.export_session_string()}`"
        )
        print(
            "تم بنجاح أستخراج كود سيشن البايروجرام"
            "ستجد الكود في الرسائل المحفوظة في التليجرام"
        )

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
