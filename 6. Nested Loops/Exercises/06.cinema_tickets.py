student_tickets_counter = 0
kid_tickets_counter = 0
standart_tickets_counter = 0
total_tickets_counter = 0
command = input()
while command != "Finish":
    movie_name = command
    free_places = int(input())
    sold_tickets = 0
    total_places = free_places
    while free_places > 0:
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets_counter += 1
        elif ticket_type == "standard":
            standart_tickets_counter += 1
        elif ticket_type == "kid":
            kid_tickets_counter += 1
        free_places -= 1
        sold_tickets += 1
        total_tickets_counter += 1
    percent_full_hall = sold_tickets / total_places * 100
    print(f"{movie_name} - {percent_full_hall:.2f}% full.")
    command = input()
students_percent = student_tickets_counter / total_tickets_counter * 100
kids_percent = kid_tickets_counter / total_tickets_counter * 100
standard_percent = standart_tickets_counter / total_tickets_counter * 100
print(f"Total tickets: {total_tickets_counter}")
print(f"{students_percent:.2f}% student tickets.")
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kids_percent:.2f}% kids tickets.")
