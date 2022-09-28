/*****************************************************************************
 *
 *     This file is part of Purdue CS 536.
 *
 *     Purdue CS 536 is free software: you can redistribute it and/or modify
 *     it under the terms of the GNU General Public License as published by
 *     the Free Software Foundation, either version 3 of the License, or
 *     (at your option) any later version.
 *
 *     Purdue CS 536 is distributed in the hope that it will be useful,
 *     but WITHOUT ANY WARRANTY; without even the implied warranty of
 *     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *     GNU General Public License for more details.
 *
 *     You should have received a copy of the GNU General Public License
 *     along with Purdue CS 536. If not, see <https://www.gnu.org/licenses/>.
 *
 *****************************************************************************/

/*
 * server.c
 * Name: Deepak Maurya
 * PUID: 0030191785
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netdb.h>
#include <netinet/in.h>
#include <errno.h>

#define QUEUE_LENGTH 10
#define RECV_BUFFER_SIZE 2048

/* TODO: server()
 * Open socket and wait for client to connect
 * Print received message to stdout
 * Return 0 on success, non-zero on failure
 */
int server(char *server_port)
{
  int server_sock, client_sock;
  unsigned short port;
  struct sockaddr_in server_addr, client_addr; 
  socklen_t addr_size; 
  char buffer[RECV_BUFFER_SIZE]; 
  int n, len; 

  port = (unsigned short) atoi(server_port);

  server_sock = socket(AF_INET, SOCK_STREAM, 0);
  if (server_sock < 0){
  	perror("Server socket error");
  	exit(1);
  }

  printf("TCP server socket created\n");

  memset(&server_addr, '\0', sizeof(server_addr)); 
  server_addr.sin_family = AF_INET; 
  server_addr.sin_addr.s_addr = INADDR_ANY; 
  server_addr.sin_port = htons(port);

  n = bind(server_sock, (struct sockaddr*)&server_addr, sizeof(server_addr));
  if (n < 0){
  	perror("server not able to bind");
  	exit(1);
  }
  printf("Server bind to the port");

  listen(server_sock, QUEUE_LENGTH);
  printf("server is listening \n");

  while(1){
  	addr_size = sizeof(client_addr); 
  	client_sock = accept(server_sock, (struct sockaddr*)&client_addr, &addr_size);
  	printf("client connected\n");

  	bzero(buffer, RECV_BUFFER_SIZE);
  	
  	while(len = recv(client_sock, buffer, sizeof(buffer), 0)){
  		fputs(buffer, stdout);
      // printf("max limit reached \n");
      fflush(stdout);
    }
  	close(client_sock);
  }

  return 0;
}

/*
 * main():
 * Parse command-line arguments and call server function
 */
int main(int argc, char **argv)
{
  char *server_port;

  if (argc != 2)
  {
    fprintf(stderr, "Usage: ./server-c (server port)\n");
    exit(EXIT_FAILURE);
  }

  server_port = argv[1];
  return server(server_port);
}
