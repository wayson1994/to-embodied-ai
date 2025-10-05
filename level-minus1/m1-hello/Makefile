#=========== Compliers & Flags ===========
CC			:= gcc
CFLAGS		:= -Wall -Wextra -g -std=gnu11
CPP			:= g++
CPPFLAGS	:= -Wall -Wextra -g -std=c++17

# Directory layout
BUILD_DIR	:= build
$(shell mkdir -p $(BUILD_DIR))
C_SRC_DIR	:= src/c
CPP_SRC_DIR := src/cpp

#=========== Python ==========
PY_SRC_DIR	:= src/py
PY_SOURCES	:= $(wildcard $(PY_SRC_DIR)/*.py)
PY_TARGET	:= $(BUILD_DIR)/main_py.log

$(PY_TARGET): $(PY_SOURCES)
	@mkdir -p $(BUILD_DIR)
	@for f in $(PY_SOURCES); do \
		echo "===== Python $$f ====="; \
		python3 "$$f"; \
	done > $@ 2>&1 || true

#=========== File Collections ===========
C_SOURCES	:= $(wildcard $(C_SRC_DIR)/*.c)
CPP_SOURCES	:= $(wildcard $(CPP_SRC_DIR)/*.cpp)
C_OBJS		:= $(patsubst %.c,$(BUILD_DIR)/%.o,$(notdir $(C_SOURCES)))
CPP_OBJS    := $(patsubst %.cpp,$(BUILD_DIR)/%.o,$(notdir $(CPP_SOURCES)))

C_TARGET	:= $(BUILD_DIR)/main_c
CPP_TARGET	:= $(BUILD_DIR)/main_cpp

#=========== Default Target ===========
.PHONY		:  all run run-c run-cpp run-py clean
all			:  $(C_TARGET) $(CPP_TARGET) run-py

#---------- C Compilation ----------
$(C_TARGET)	:  $(C_OBJS)
	$(CC) $(CFLAGS) $^ -o $@

$(BUILD_DIR)/%.o : $(C_SRC_DIR)/%.c
	$(CC) $(CFLAGS) -c $< -o $@

#---------- Cpp Compilation ---------
$(CPP_TARGET)	:  $(CPP_OBJS)
	$(CPP) $(CPPFLAGS) $^ -o $@

$(BUILD_DIR)/%.o : $(CPP_SRC_DIR)/%.cpp
	$(CPP) $(CPPFLAGS) -c $< -o $@

#---------- Run ----------
run			: run-c run-cpp run-py

run-c		: $(C_TARGET)
	@echo "===== RunningC ====="
	@$(C_TARGET)
	@echo "=====  Finish  ====="

run-cpp		: $(CPP_TARGET)
	@echo "===== RunningCpp ====="
	@$(CPP_TARGET)
	@echo "=====   Finish   ====="

run-py		: 
	@echo "===== RunningPy ====="
	@python3 $(PY_SOURCES)
	@echo "=====  Finish   ====="

#---------- Clean ----------
clean		:
	$(RM) -r $(BUILD_DIR)