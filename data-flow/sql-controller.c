#include <mysql/mysql.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void usage() {
	printf("\n\n1st argument is password\n 2nd argument is command to run\n\n");
}

main() {
	printf("MySQL client version: %s\n");
	exit(0);
}
