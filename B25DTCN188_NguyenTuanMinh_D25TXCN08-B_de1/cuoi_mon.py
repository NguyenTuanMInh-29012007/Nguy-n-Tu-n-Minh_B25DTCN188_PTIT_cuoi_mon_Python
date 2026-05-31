import json

f = open("B25DTCN188_NguyenTuanMinh_D25TXCN08-B_de1/data.json", "r", encoding="utf-8")
player_list = json.load(f)
f.close()

while True:

    print(f"""
    {'='*50}
    |                QUẢN LÝ CẦU THỦ                 |
    {'='*50}
    |  1. Hiển thị danh sách cầu thủ                 |
    |  2. Thêm mới cầu thủ                           |
    |  3. Cập nhật thông tin cầu thủ                 |
    |  4. Xóa cầu thủ                                |
    |  5. Tìm kiếm cầu thủ                           |
    |  6. Sắp xếp danh sách cầu thủ                  |
    |  7. Thống kê cầu thủ theo danh hiệu            |
    |  8. Thống kê số lượng cầu thủ theo danh hiệu   |
    |  9. Cầu thủ có nhiều/ít danh hiệu nhất         |
    |  10. Thoát                                     |
    {'='*50}""")
    choice = input("Nhập lựa chọn: ")

    match choice:
        case "1":
            if len(player_list) == 0:
                print("Danh sách hiện đang trống!")

            else:
                print("-" * 85)
                print(f"{'Mã CT':<7} | {'Tên Cầu Thủ':<15} | {'Số Trận':<7} | {'Bàn Thắng':<10} | {'Kiến Tạo':<8} | {'Điểm TT':<8} | {'Danh Hiệu':^10}")
                print("-" * 85)

                for player in player_list:
                    print(f"{player['ma_ct']:<7} | {player['ten_ct']:<15} | {player['so_tran']:<7} | {player['ban_thang']:<10} | {player['kien_tao']:<8} | {player['diem_thanh_tich']:<8} | {player['danh_hieu']:^10}")
                print("-" * 85)

        case "2":
            ma_ct = input("Nhập Mã cầu thủ: ").upper().strip()

            check = False
            for player in player_list:
                if player["ma_ct"] == ma_ct:
                    check = True
                    break

            if check == True:
                print("MÃ cầu thủ đó đã tồn tại!")

            else:
                ten_ct = input("Nhập TÊN cầu thủ: ").title().strip()

                so_tran = int(input("Nhập số trận: "))
                ban_thang = int(input("Nhập số bàn thắng: "))
                kien_tao = int(input("Nhập số kiến tạo: "))

                if so_tran < 0:
                    print("Số trận nhập KHÔNG hợp lệ!")
                elif ban_thang < 0:
                    print("Số bàn thắng nhập không hợp lệ!")
                elif kien_tao < 0:
                    print("Số kiến tạo nhập không hợp lệ!")
                else:
                    diem_thanh_tich = (ban_thang * 2) + kien_tao

                    if diem_thanh_tich > 40:
                        danh_hieu = "Vàng"
                    elif diem_thanh_tich > 20:
                        danh_hieu = "Bạc"
                    else:
                        danh_hieu = "Đồng"

                    player = {
                        "ma_ct": ma_ct,
                        "ten_ct": ten_ct,
                        "so_tran": so_tran,
                        "ban_thang": ban_thang,
                        "kien_tao": kien_tao,
                        "diem_thanh_tich": diem_thanh_tich,
                        "danh_hieu": danh_hieu
                    }

                    player_list.append(player)

                    f = open("data.json", "w", encoding="utf-8")
                    json.dump(player_list, f, ensure_ascii=False, indent=4)
                    f.close()

                    print("Thêm thành công!")

        case "3":
            ma_ct = input("Nhập MÃ cầu thủ cần sửa: ").upper().strip()

            check = False
            for player in player_list:
                if player["ma_ct"] == ma_ct:
                    check = True

                    ban_thang = int(input("Nhập số bàn thắng mới: "))
                    kien_tao = int(input("Nhập số kiến tạo mới: "))

                    if ban_thang < 0 or kien_tao < 0:
                        print("Số liệu không hợp lệ!")
                        break

                    player["ban_thang"] = ban_thang
                    player["kien_tao"] = kien_tao
                    player["diem_thanh_tich"] = (ban_thang * 2) + kien_tao

                    if player["diem_thanh_tich"] > 40:
                        player["danh_hieu"] = "Vàng"
                    elif player["diem_thanh_tich"] > 20:
                        player["danh_hieu"] = "Bạc"
                    else:
                        player["danh_hieu"] = "Đồng"

                    f = open("data.json", "w", encoding="utf-8")
                    json.dump(player_list, f, ensure_ascii=False, indent=4)
                    f.close()

                    print("Cập nhật thành công!")
                    break

            if check == False:
                print("Không tìm thấy cầu thủ bạn vừa nhập!")

        case "4":
            ma_ct = input("Nhập MÃ cầu thủ cần xóa: ").upper().strip()

            check = False
            for player in player_list:
                if player["ma_ct"] == ma_ct:
                    check = True

                    confirm = input("Bạn có chắc chắn muốn xóa? (y/n): ")
                    if confirm == "y":
                        player_list.remove(player)

                        f = open("data.json", "w", encoding="utf-8")
                        json.dump(player_list, f, ensure_ascii=False, indent=4)
                        f.close()

                        print(f"Đã xóa thành công {player['ten_ct']}!")
                    break

            if check == False:
                print("Không tìm thấy cầu thủ bạn vừa nhập!")

        case "5":
            keyword = input("Nhập MÃ CT hoặc tên cần tìm: ").upper().strip()

            check = False
            print("-" * 60)
            print(f"{'Mã CT':<7} | {'Tên':<20} | {'Điểm TT':<8} | {'Danh hiệu':<10}")

            for player in player_list:
                if keyword in player["ma_ct"].upper() or keyword in player["ten_ct"].upper():
                    check = True
                    print(f"{player['ma_ct']:<7} | {player['ten_ct']:<20} | {player['diem_thanh_tich']:<8} | {player['danh_hieu']:<10}")

            if check == False:
                print("Không tìm thấy MÃ CT bạn vừa nhập!")

        case "6":
            print("""
        1. Sắp xếp theo điểm thành tích giảm dần
        2. Sắp xếp theo số bàn thắng giảm dần""")
            choose = input("Mời bạn nhập lựa chọn: ")

            if choose == "1":
                for i in range(len(player_list) - 1):
                    for j in range(i + 1, len(player_list)):
                        if player_list[i]["diem_thanh_tich"] < player_list[j]["diem_thanh_tich"]:
                            temp = player_list[i]
                            player_list[i] = player_list[j]
                            player_list[j] = temp
                print("Sắp xếp thành công! Hãy chọn lại chức năng 1 để XEM.")

            elif choose == "2":
                for i in range(len(player_list) - 1):
                    for j in range(i + 1, len(player_list)):
                        if player_list[i]["ban_thang"] < player_list[j]["ban_thang"]:
                            temp = player_list[i]
                            player_list[i] = player_list[j]
                            player_list[j] = temp
                print("Sắp xếp thành công! Hãy chọn lại chức năng 1 để XEM.")

        case "7":
            if len(player_list) == 0:
                print("Danh sách trống!")
            else:
                print("-" * 50)
                print(f"{'Mã CT':<7} | {'Tên Cầu Thủ':<22} | {'Danh Hiệu':^12}")
                print("-" * 50)

                for player in player_list:
                    print(f"{player['ma_ct']:<7} | {player['ten_ct']:<22} | {player['danh_hieu']:^12}")
                    
                print("-" * 50)

        case "8":
            vang = 0
            bac = 0
            dong = 0

            for player in player_list:
                danh_hieu = player["danh_hieu"].lower().strip()
                if danh_hieu == "vàng":
                    vang += 1
                elif danh_hieu == "bạc":
                    bac += 1
                else:
                    dong += 1

            print("-" * 40)
            print(f"{'Danh hiệu':<15} | {'Số lượng':^10}")
            print("-" * 40)
            print(f"{'Vàng':<15} | {vang:^10}")
            print(f"{'Bạc':<15} | {bac:^10}")
            print(f"{'Đồng':<15} | {dong:^10}")
            print("-" * 40)

        case "9":
            if len(player_list) == 0:
                print("Danh sách trống!")
            else:
                max_player = player_list[0]
                min_player = player_list[0]

                for player in player_list:
                    if player["diem_thanh_tich"] > max_player["diem_thanh_tich"]:
                        max_player = player
                    if player["diem_thanh_tich"] < min_player["diem_thanh_tich"]:
                        min_player = player

                print("-" * 80)
                print(f"{'Danh hiệu':<15} | {'Mã CT':<7} | {'Tên Cầu Thủ':<20} | {'Điểm TT':<7} | {'Danh Hiệu':^10}")
                print("-" * 80)
                print(f"{'Nhiều nhất':<15} | {max_player['ma_ct']:<7} | {max_player['ten_ct']:<20} | {max_player['diem_thanh_tich']:<7} | {max_player['danh_hieu']:^10}")
                print(f"{'Ít nhất':<15} | {min_player['ma_ct']:<7} | {min_player['ten_ct']:<20} | {min_player['diem_thanh_tich']:<7} | {min_player['danh_hieu']:^10}")
                print("-" * 80)

        case "10":
            print("Cảm ơn bạn đã sử dùng Dịch Vụ! Hệ thống đang đăng xuất...")
            break

        case _:
            print("Lựa chọn không hợp lệ! Vui lòng nhập từ (1-10): ")
