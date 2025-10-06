CC			:= gcc
CFLAGS		:= -Wall -Wextra -g -std=gnu11

BUILD_DIR	:= build
SRC_DIR		:= src

SRC			:= $(wildcard $(SRC_DIR)/*.c);
TARGET		:= $(BUILD_DIR)/main

.PHONY		: all run clean
all			: $(TARGET) 

$(TARGET) : $(SRC)
	@mkdir -p $(BUILD_DIR)
	$(CC) $(CFLAGS) $^ -o $@

run			: $(TARGET)
	@echo "===== Running ====="
	$(TARGET)
	@echo "===== Finish  ====="

clean		:
	$(RM) -r $(BUILD_DIR)