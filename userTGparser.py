import time
from pyrogram import Client
from pyrogram.enums import UserStatus


api_id = #you_id_id
api_hash = #"you_hash_api"
link = #"tg_linl"
filter_words = ["word1", "word2", "word3", ...]


output_file = "user_info.txt"
output_file_taxi = "user_info_filter.txt"


app = Client("my_account", api_id=api_id, api_hash=api_hash)

def create_stylized_user_info(user_info, message_text=None):

    lines = [
        f"Аккаунт: {user_info['username']}",
        f"Имя: {user_info['first_name']}",
        f"Номер: {user_info['phone_number']}",
        f"Статус: {user_info['status']}"
    ]
    
    if message_text:
        lines.append(f"Сообщение: {message_text}")
    
    max_length = max(len(line) for line in lines)
    

    border = '+' + '-' * (max_length + 2) + '+'
    

    user_info_str = (
        f"{border}\n"
        f"| {lines[0].ljust(max_length)} |\n"
        f"| {lines[1].ljust(max_length)} |\n"
        f"| {lines[2].ljust(max_length)} |\n"
        f"| {lines[3].ljust(max_length)} |\n"
    )
    
    if message_text:
        user_info_str += f" {lines[4].ljust(max_length)} \n"
    
    user_info_str += f"{border}\n"
    
    return user_info_str

async def get_usernames():
    async with app:
        
        chat = await app.get_chat(link)
        
        user_infos = set()  
        user_infos_taxi = set()  
        seen_usernames = set()  
        seen_message_texts = set()  
        
        async for message in app.get_chat_history(chat.id):
            user = message.from_user
            if user and user.username and user.username not in seen_usernames:
                seen_usernames.add(user.username) 
                
                try:
                    member = await app.get_chat_member(chat.id, user.id)
                    common_chats_count = member.common_chats_count if member else "N/A"
                except:
                    common_chats_count = "N/A"
                
                status = str(user.status) if hasattr(user, 'status') else "N/A"
                if user.status == UserStatus.RECENTLY:
                    status = "был(а) недавно"

                user_info = {
                    "username": f"@{user.username}",
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "phone_number": user.phone_number if hasattr(user, 'phone_number') else "None",
                    "status": status,
                    "common_chats_count": common_chats_count
                }
                
                user_info_str = create_stylized_user_info(user_info)

                if user_info_str not in user_infos:
                    user_infos.add(user_info_str)
                    with open(output_file, "a", encoding="utf-8") as f:
                        f.write(user_info_str)
                    print(f"Добавил:\n {user_info_str}")

                if message.text and message.text not in seen_message_texts:
                    seen_message_texts.add(message.text)
                    if any(word in message.text.lower() for word in filter_words):
                        user_info_taxi_str = create_stylized_user_info(user_info, message.text)
                        if user_info_taxi_str not in user_infos_taxi:
                            user_infos_taxi.add(user_info_taxi_str)
                            with open(output_file_taxi, "a", encoding="utf-8") as f:
                                f.write(user_info_taxi_str)
                            print(f"Добавил в filter:\n {user_info_taxi_str}")

            time.sleep(0.5)

if __name__ == "__main__":
    app.run(get_usernames())
