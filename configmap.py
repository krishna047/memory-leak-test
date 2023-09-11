apiVersion: v1
kind: ConfigMap
metadata:
  name: pyhton-scripts-cofigmap
data:
  memory_increase.py: |
    import time

    def allocate_memory(mb):
        data = bytearray(mb * 1024 * 1024)
        return data

    if __name__ == "__main__":
        mb_to_allocate = 10
        while True:
            allocate_memory(mb_to_allocate)
            mb_to_allocate += 10
            print(f"Allocated {mb_to_allocate} MB memory.")
            time.sleep(5)