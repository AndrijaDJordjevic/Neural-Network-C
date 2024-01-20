##
## EPITECH PROJECT, 2023
## makefile
## File description:
## makefile
##

NAME = my_torch

all: $(NAME)

$(NAME): main.py
	@cp $< $@
	@chmod 777 $(NAME)

clean:
	@rm -f mypgp

fclean: clean
	@rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re