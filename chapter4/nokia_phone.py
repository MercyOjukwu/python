main_menu = int(input("Enter 1 to open main menu: "))
print("========================================")


if main_menu == 1:
    print("List of menu functions: \n"
          "  1.Phone book \n"
          "  2.Messages \n"
          "  3.Call register \n"
          )
    inner = int(input("Enter a number to view particular menu functions:"))
    print("========================================")


    if inner == 1:
        print("1.Phone Book > \n"
              "  a.Search \n"
              "  b.Service Nos. \n"
              "  c.Add name \n"
              "  d.Erase \n"
              "  e.Edit \n"
              "  f.Assign tone \n"
              "  g.Send b'card \n"
              )

        inside_phone = input("Enter option for phone book functions: ")
        if inside_phone == "a":
            print("  a.Search by name\n"
                  "  b.Search by contact \n"
                  )
            outside_phone = input("Enter 1 to exit search option: ")
            if outside_phone == 1:
                print("1.Phone Book > \n"
                      "  a.Search \n"
                      "  b.Service Nos. \n"
                      "  c.Add name \n"
                      "  d.Erase \n"
                      "  e.Edit \n"
                      "  f.Assign tone \n"
                      "  g.Send b'card \n")
            elif outside_phone != 1:
                print("Why you so stubborn? ")
            back_to_main = input("Enter 1 to exit phone book: ")
            if back_to_main == 1:
                print("List of menu functions: \n"
                      "  1.Phone book \n"
                      "  2.Messages \n"
                      "  3.Call register \n")
            else:
                print("Why you so stubborn?")
        elif inside_phone == "b":
            print("The service numbers include> \n"
                  "  +234 802 357 4501 \n"
                  "  +14 009 1234 12 \n"
                  "  +123 903 458 98")
        elif inside_phone == "c":
            print("This service is currently unavailable.")
        elif inside_phone == "d":
            print("This service is currently unavailable.")
        elif inside_phone == "e":
            print("This service is currently unavailable.")
        elif inside_phone == "f":
            print("This service is currently unavailable.")
        elif inside_phone == "g":
            print("This service is currently unavailable.")

    elif inner == 2:
        print("2.Messages > \n"
              "  a.Write Messages \n"
              "  b.Inbox \n"
              "  c.Outbox \n"
              "  d.Info Service \n"
              "  e.Info service \n"
              "  f.Voice mailbox number"
              )
    elif inner == 3:
        print("3.CallRegister > \n"
              "  a.Received calls \n"
              "  b.Dialled Numbers \n"
              "  c.Erase recent call list \n"
              "  d.Show call duration \n"
              "  e.Show call costs \n"
              )
    else:
        print("Menu can only open with command")

else:
    print("Main menu function can only open with listed command")
