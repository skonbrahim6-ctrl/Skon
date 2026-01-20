# نظام الطابور لإدارة تشغيل الأغاني
queue = {}

def add_to_queue(chat_id, title, url, user):
    if chat_id not in queue:
        queue[chat_id] = []
    queue[chat_id].append({"title": title, "url": url, "user": user})
    return len(queue[chat_id])

def get_queue(chat_id):
    if chat_id in queue:
        return queue[chat_id]
    return []

def clear_queue(chat_id):
    if chat_id in queue:
        queue.pop(chat_id)
                  
