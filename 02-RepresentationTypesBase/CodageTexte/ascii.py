#coding -*- ascii-*-
def main():
	for i in range(256):
		print(str(i) + " : " + chr(i), end = "\t" )
		if (i + 1) % 8 == 0:
			print()
	return 0

if __name__ == "__main__":
    main()