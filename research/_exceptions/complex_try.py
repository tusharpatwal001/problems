import time


def serve_chai(flavor):
    try:
        print(f"Prepraing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("We don't know that flavor")
    except ValueError as e:
        print("Error: ", e)
    else:
        time.sleep(1)
        print(f"{flavor} chai is served")
    finally:
        print("Next customer please")


serve_chai("masala")
serve_chai("unknown")
