# packing
def data(**kwargs):
    for key, values in kwargs.items():
        print(f"{key}: {values}")


result = data(first_name="Binita", last_name="Adhikari", Age=22)
