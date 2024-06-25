CC=gcc
CFLAGS=-Wall -g
TARGET=main
SRC=main_copy.c cities.c dijkstra.c adjlist.c

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) $(SRC) -o $(TARGET)

clean:
	rm -f $(TARGET)
