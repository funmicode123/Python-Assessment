print("Welcome to your Nokia phone")

print("""
1. Phone book
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Games
9. Calculator
10. Reminder
11. Clock
12. Profiles
13. SIM services
""")

menu_option = int(input("Select an option: "))

match menu_option:
    case 1:
        print("Phone book")
        print("""
        1. Search
        2. Service Nos
        3. Add name
        4. Erase
        5. Edit
        6. Assign tone
        7. Send b'card
        8. Options
        9. Speed dials
        10. Voice tags
        """)
        phone_book_list = int(input("Select an option: "))
        
        match phone_book_list:
            case 1:
                print("Search")
            case 2:
                print("Service Nos")
            case 3:
                print("Add name")
            case 4:
                print("Erase")
            case 5:
                print("Edit")
            case 6:
                print("Assign tone")
            case 7:
                print("Send b'card")
            case 8:
                print("Options")
                print("""
                1. Type of view
                2. Memory status
                """)
                options_option = int(input("Select an option: "))
                
                match options_option:
                    case 1:
                        print("Type of view")
                    case 2:
                        print("Memory status")
                    case _:
                        print("Invalid option in options")
            case 9:
                print("Speed dials")
            case 10:
                print("Voice tags")
            case _:
                print("Invalid entry in phone book")
                
    case 2:
        print("Messages")
        print("""
        1. Write messages
        2. Inbox
        3. Outbox
        4. Picture messages
        5. Templates
        6. Smileys
        7. Message settings
            1. Set
                1. Message centre number
                2. Messages sent as
                3. Message validity
            2. Common
                1. Delivery reports
                2. Reply via same centre
                3. Character support
        8. Info service
        9. Voice mailbox number
        10. Service command editor
        """)
        message_list = int(input("Select an option: "))
        
        match message_list:
            case 1:
                print("Write messages")
            case 2:
                print("Inbox")
            case 3:
                print("Outbox")
            case 4:
                print("Picture messages")
            case 5:
                print("Templates")
            case 6:
                print("Smileys")
            case 7:
                print("Message settings")
                print("""
                1. Set
                2. Common
                """)
                message_setting = int(input("Select an option: "))
                
                match message_setting:
                    case 1:
                        print("Set")
                        print("""
                        1. Message centre number
                        2. Messages sent as
                        3. Message validity
                        """)
                        set_list = int(input("Select an option: "))
                        match set_list:
                            case 1:
                                print("Message centre number")
                            case 2:
                                print("Messages sent as")
                            case 3:
                                print("Message validity")
                            case _:
                                print("Invalid entry in set options")
                    case 2:
                        print("Common")
                        print("""
                        1. Delivery reports
                        2. Reply via same centre
                        3. Character support
                        """)
                        common_list = int(input("Select an option: "))
                        match common_list:
                            case 1:
                                print("Delivery reports")
                            case 2:
                                print("Reply via same centre")
                            case 3:
                                print("Character support")
                            case _:
                                print("Invalid entry in common options")
            case 8:
                print("Info service")
            case 9:
                print("Voice mailbox number")
            case 10:
                print("Service command editor")
            case _:
                print("Invalid entry in messages")
                
    case 3:
        print("Chat")
    case 4:
        print("Call register")
        print("""
        1. missed calls
        2. received calls
        3. dialled number
        4. erase recent call lists
        5. show call duration
            1. last call duration
            2. all calls' duration
            3. received calls' duration
            4. dialled calls' duration
            5. clear timers
        6. show call costs
            1. last call cost
            2. all calls' cost
            3. clear counters
        7. call cost settings
            1. call cost limit
            2. show costs in
        8. prepaid credit
        """)
        call_register_list = int(input("Select an option: "))
        match call_register_list:
            case 1:
                print("missed calls")
            case 2:
                print("received calls")
            case 3:
                print("dialled number")
            case 4:
                print("erase recent call lists")
            case 5:
                print("show call duration")
                print("""
                1. last call duration
                2. all calls' duration
                3. received calls' duration
                4. dialled calls' duration
                5. clear timers
                """)
                show_call_duration_list = int(input("Select an option: "))
                match show_call_duration_list:
                    case 1:
                        print("last call duration")
                    case 2:
                        print("all calls' duration")
                    case 3:
                        print("received calls' duration")
                    case 4:
                        print("dialled calls' duration")
                    case 5:
                        print("clear timers")
                    case _:
                        print("invalid entry")
            case 6:
                print("show call costs")
                print("""
                1. last call cost
                2. all calls' cost
                3. clear counters
                """)
                show_call_costs_list = int(input("Select an option: "))
                match show_call_costs_list:
                    case 1:
                        print("last call cost")
                    case 2:
                        print("all calls' cost")
                    case 3:
                        print("clear counters")
                    case _:
                        print("invalid entry")
            case 7:
                print("call cost settings")
                print("""
                1. call cost limit
                2. show costs in
                """)
                call_cost_settings = int(input("Select an option: "))
                match call_cost_settings:
                    case 1:
                        print("call cost limit")
                    case 2:
                        print("show costs in")
                    case _:
                        print("invalid entry")
            case 8:
                print("prepaid credit")
            case _:
                print("invalid entry")
    case 5:
        print("Tones")
        print("""
        1. ringing tone
        2. ringing volume
        3. incoming call alert
        4. composer
        5. message alert tone
        6. keypad tones
        7. warning and game tones
        8. vibrating alert
        9. screen saver
        """)
        tones_list = int(input("Select an option: "))
        match tones_list:
            case 1:
                print("ringing tone")
            case 2:
                print("ringing volume")
            case 3:
                print("incoming call alert")
            case 4:
                print("composer")
            case 5:
                print("message alert tone")
            case 6:
                print("keypad tones")
            case 7:
                print("warning and game tones")
            case 8:
                print("vibrating alert")
            case 9:
                print("screen saver")
            case _:
                print("invalid entry")
    case 6:
        print("Settings")
        print("""
        1. call settings
            1. automatic redial
            2. speed dialling
            3. call waiting options
            4. own number sending
            5. phone line in use
            6. automatic answer
        2. phone settings
            1. language
            2. cell info display
            3. welcome note
            4. network selection
            5. lights
            6. confirm sim service actions
        3. security settings
            1. pin code request
            2. call barring service
            3. fixed dialling
            4. closed user group
            5. phone security
            6. change access codes
        4. restore factory settings
        """)
        settings_list = int(input("Select an option: "))
        match settings_list:
            case 1:
                print("call settings")
                print("""
                1. automatic redial
                2. speed dialling
                3. call waiting options
                4. own number sending
                5. phone line in use
                6. automatic answer
                """)
                call_settings_list = int(input("Select an option: "))
                match call_settings_list:
                    case 1:
                        print("automatic redial")
                    case 2:
                        print("speed dialling")
                    case 3:
                        print("call waiting options")
                    case 4:
                        print("own number sending")
                    case 5:
                        print("phone line in use")
                    case 6:
                        print("automatic answer")
                    case _:
                        print("invalid entry")
            case 2:
                print("phone settings")
                print("""
                1. language
                2. cell info display
                3. welcome note
                4. network selection
                5. lights
                6. confirm sim service actions
                """)
                phone_settings_list = int(input("Select an option: "))
                match phone_settings_list:
                    case 1:
                        print("language")
                    case 2:
                        print("cell info display")
                    case 3:
                        print("welcome note")
                    case 4:
                        print("network selection")
                    case 5:
                        print("lights")
                    case 6:
                        print("confirm sim service actions")
                    case _:
                        print("invalid entry")
            case 3:
                print("security settings")
                print("""
                1. pin code request
                2. call barring service
                3. fixed dialling
                4. closed user group
                5. phone security
                6. change access codes
                """)
                security_settings_list = int(input("Select an option: "))
                match security_settings_list:
                    case 1:
                        print("pin code request")
                    case 2:
                        print("call barring service")
                    case 3:
                        print("fixed dialling")
                    case 4:
                        print("closed user group")
                    case 5:
                        print("phone security")
                    case 6:
                        print("change access codes")
                    case _:
                        print("invalid entry")
            case 4:
                print("restore factory settings")
            case _:
                print("invalid entry")
    case 7:
        print("Call divert")
    case 8:
        print("Games")
    case 9:
        print("Calculator")
    case 10:
        print("Reminder")
    case 11:
        print("Clock")
        print("""
        1. alarm clock
        2. clock settings
        3. date settings
        4. stopwatch
        5. countdown timer
        6. auto update of date and time
        """)
        clock_list = int(input("Select an option: "))
        match clock_list:
            case 1:
                print("alarm clock")
            case 2:
                print("clock settings")
            case 3:
                print("date settings")
            case 4:
                print("stopwatch")
            case 5:
                print("countdown timer")
            case 6:
                print("auto update of date and time")
            case _:
                print("invalid entry")
    case 12:
        print("Profiles")
    case 13:
        print("SIM services")
    case _:
        print("Invalid menu option")
