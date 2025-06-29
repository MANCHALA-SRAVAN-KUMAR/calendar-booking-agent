import calendar
from datetime import datetime
import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "calendar_data.json")

def read_appointments():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            data = json.load(f)
            return data
        except json.JSONDecodeError:
            return []

def write_appointments(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_available_slots(date_str):
    slots = ["09:00", "10:00", "11:00", "14:00", "15:00", "16:00"]
    appointments = read_appointments()
    booked_times = [appt["time"] for appt in appointments if appt["date"] == date_str]
    available = [slot for slot in slots if slot not in booked_times]
    return available

def book_slot(date_str, time_str):
    appointments = read_appointments()
    for appt in appointments:
        if appt["date"] == date_str and appt["time"] == time_str:
            return False
    appointments.append({"date": date_str, "time": time_str})
    write_appointments(appointments)
    return True

def get_booked_appointments():
    return read_appointments()

def get_month_calendar(month=None, year=None):
    now = datetime.now()
    if year is None:
        year = now.year
    if month is None:
        month = now.month
    cal = calendar.monthcalendar(year, month)
    html = f"<h3>📅 {calendar.month_name[month]} {year}</h3>"
    html += "<table border='1' style='border-collapse: collapse; text-align: center;'>"
    html += "<tr>" + "".join(f"<th>{day}</th>" for day in ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]) + "</tr>"
    for week in cal:
        html += "<tr>"
        for day in week:
            day_display = day if day != 0 else "&nbsp;"
            html += f"<td style='padding: 5px;'>{day_display}</td>"
        html += "</tr>"
    html += "</table>"
    return html

def get_year_calendar(year=None):
    now = datetime.now()
    if year is None:
        year = now.year
    html = f"<h3>📅 Year: {year}</h3>"
    for month in range(1, 13):
        html += get_month_calendar(month, year) + "<br/>"
    return html
