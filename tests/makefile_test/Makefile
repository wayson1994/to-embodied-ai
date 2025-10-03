CC 		= gcc
CFLAGS 	= -Wall -O2
TARGET	= app
SRCS	= main.c add.c
OBJS	= $(SRCS:.c=.o)

default	: $(TARGET)

%.o : %.c
	$(CC) $(CFLAGS) -c $< -o $@

$(TARGET) : $(OBJS)
	$(CC) $(OBJS) -o $(TARGET)


.PHONY : clean
clean :
	rm -f $(OBJS) $(TARGET)