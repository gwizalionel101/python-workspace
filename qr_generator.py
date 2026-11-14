
import qrcode

while True:
    print("\n------ QR CODE GENERATOR ------")
    print("1. Link or text")
    print("2. Contact card")
    print("3. WiFi")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        text = input("Enter link or text: ")
        file = input("File name: ")

        img = qrcode.make(text)
        img.save(file + ".png")

        print("Saved:", file + ".png")

    elif choice == "2":
        first = input("Enter firstname: ")
        last = input("Enter lastname: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        full = first + " " + last

        card = ["BEGIN:VCARD", "VERSION:3.0"]
        card.append("N:" + last + ";" + first)
        card.append("FN:" + full)
        card.append("TEL:" + phone)
        card.append("EMAIL:" + email)
        card.append("END:VCARD")

        vcard = "\n".join(card)

        img = qrcode.make(vcard)
        img.save("contact_qr.png")

        print("Saved: contact_qr.png")

    elif choice == "3":
        ssid = input("Enter wifi name: ")
        pas = input("Enter wifi password: ")

        wifi = "WIFI:T:WPA;S:" + ssid
        wifi = wifi + ";P:" + pas + ";;"

        img = qrcode.make(wifi)
        img.save("wifi_qr.png")

        print("Saved: wifi_qr.png")

    elif choice == "4":
        print("Bye!")
        break

    else:
        print("Invalid option")
