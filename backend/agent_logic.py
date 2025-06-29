from calendar_utils import (
    get_available_slots,
    book_slot,
    get_month_calendar,
    get_year_calendar,
    get_booked_appointments,
)
from utils import extract_date_time

def process_user_message(message: str) -> str:
    message = message.lower()

    if "help" in message:
        return (
            "🆘 How to Use:\n"
            "Type 'show me calendar' to view current month\n"
            "'this year calendar' shows the full year\n"
            "Say 'book appointment' or 'book slot' to start booking\n"
            "Provide date (YYYY-MM-DD) and time (e.g., 14:00)"
        )

    if "show me calendar" in message:
        return get_month_calendar()

    if "this year calendar" in message:
        return get_year_calendar()

    for month_name in [
        "january", "february", "march", "april", "may", "june",
        "july", "august", "september", "october", "november", "december"
    ]:
        if month_name in message:
            from datetime import datetime
            year = datetime.now().year
            month = {
                "january": 1, "february": 2, "march": 3, "april": 4,
                "may": 5, "june": 6, "july": 7, "august": 8,
                "september": 9, "october": 10, "november": 11, "december": 12
            }[month_name]
            return get_month_calendar(month, year)

    if "book appointment" in message or "book slot" in message:
        return "🔔 Please tell me the date (YYYY-MM-DD) and time (e.g., 14:00) you want to book."

    # Try to parse date and time
    date_time = extract_date_time(message)
    if date_time:
        date_str, time_str = date_time
        available = get_available_slots(date_str)
        if time_str:
            if time_str not in available:
                return f"⚠️ The slot {time_str} on {date_str} is not available. Available slots: {', '.join(available)}"
            success = book_slot(date_str, time_str)
            if success:
                return f"✅ Appointment booked for {date_str} at {time_str}."
            else:
                return "⚠️ That slot is already booked."
        else:
            return f"⌚ Please provide the time (e.g., 14:00) for your selected date {date_str}."
    
    if "booked appointments" in message or "show booked" in message:
        booked = get_booked_appointments()
        if not booked:
            return "📭 No appointments booked yet."
        msg = "📅 Booked Appointments:\n"
        for appt in booked:
            msg += f"- {appt['date']} at {appt['time']}\n"
        return msg

    return "🤖 Sorry, I didn't understand that. Try typing 'help' to see what I can do."
