CC      = gcc
CFLAGS  = -Wall -O2
BUILD   = ../build
TARGET  = $(BUILD)/main
SRCS    = day3_gcc_lab/hello.c
# 把 .o 也放到 build 目录
OBJS    = $(patsubst %.c,$(BUILD)/%.o,$(notdir $(SRCS)))

default: $(TARGET)

# 编译：源在 src，输出在 build
$(BUILD)/%.o : day3_gcc_lab/%.c | $(BUILD)
	$(CC) $(CFLAGS) -c $< -o $@

$(TARGET): $(OBJS)
	$(CC) $^ -o $@

# 确保 build 目录存在
$(BUILD):
	mkdir -p $(BUILD)

.PHONY: clean
clean:
	rm -rf $(BUILD)