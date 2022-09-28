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
 * client.c
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

#define SEND_BUFFER_SIZE 2048

int sendall(int s, char *buf, int *len)
{
  int total = 0;        // how many bytes we've sent
  int bytesleft = *len; // how many we have left to send
  int n;

  while(total < *len) {
    n = send(s, buf+total, bytesleft, 0);
    if (n == -1) { break; }
    total += n;
    bytesleft -= n;
    }

  *len = total; // return number actually sent here

  return n==-1?-1:0; // return -1 on failure, 0 on success
} 

/* TODO: client()
 * Open socket and send message from stdin.
 * Return 0 on success, non-zero on failure
 */
int client(char *server_ip, char *server_port)
{
  int sock;
  unsigned short port;
  struct sockaddr_in addr; 
  socklen_t addr_size; 
  char buffer[SEND_BUFFER_SIZE]; 
  int n, len;

  port = (unsigned short) atoi(server_port);

  sock = socket(AF_INET, SOCK_STREAM, 0);
  if (sock < 0){
    perror("not able to create socket in client");
    exit(1);
  }

  printf("TCP server socket created in client \n");

  memset(&addr, '\0', sizeof(addr));
  addr.sin_family = AF_INET; 
  addr.sin_port = htons(port);
  addr.sin_addr.s_addr = inet_addr(server_ip); 

  if (connect(sock, (struct sockaddr*)&addr, sizeof(addr)) < 0 ){
    perror("client could not connect to server");
    close(sock);
    exit(1);
  }
  printf("client connected to server\n");

  bzero(buffer, SEND_BUFFER_SIZE);
  while(fgets(buffer, sizeof(buffer), stdin)){
    buffer[SEND_BUFFER_SIZE - 1] = '\0';
    len = strlen(buffer) + 1;
    /* send(sock, buffer, len, 0); */
    sendall(sock, buffer, &len);
  }

  close(sock);
  printf("Client Disconnected from server");

  return 0;
}

/*
 * main()
 * Parse command-line arguments and call client function
 */
int main(int argc, char **argv)
{
  char *server_ip;
  char *server_port;

  if (argc != 3)
  {
    fprintf(stderr, "Usage: ./client-c (server IP) (server port) < (message)\n");
    exit(EXIT_FAILURE);
  }

  server_ip = argv[1];
  server_port = argv[2];
  return client(server_ip, server_port);
}
