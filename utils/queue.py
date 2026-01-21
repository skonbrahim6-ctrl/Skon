# قاموس لتخزين قائمة الانتظار لكل مجموعة
queue = {}

def add_to_queue(chat_id, title, url, user):
    """إضافة أغنية إلى الطابور"""
    if chat_id not in queue:
        queue[chat_id] = []
    queue[chat_id].append({
        "title": title, 
        "url": url, 
        "user": user
    })
    return len(queue[chat_id])

def get_queue(chat_id):
    """جلب قائمة الأغاني المنتظرة لمجموعة معينة"""
    return queue.get(chat_id, [])

def pop_queue(chat_id):
    """حذف الأغنية الأولى بعد انتهاء تشغيلها/تحميلها"""
    if chat_id in queue and len(queue[chat_id]) > 0:
        return queue[chat_id].pop(0)
    return None

def clear_queue(chat_id):
    """تفريغ الطابور بالكامل"""
    if chat_id in queue:
        queue.pop(chat_id, None)
        return True
    return False
    
