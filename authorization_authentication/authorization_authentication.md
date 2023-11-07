# Authentication - Identification

![client_send_request_to_server](images/client_send_request_to_server.png)

# If authenticate(request) is OK

## 1. Server create session in database

![server_create_session](images/server_create_session.png)

## 2. Server send session_id in cookies

![server_send_cookies](images/server_send_cookies.png)

## 3. Client save domain : cookies and send them with each request

![client_save_cookies](images/client_save_cookies.png)

## 4. When user logout the server delete session from database

![when_user_logout_session_deleted](images/when_user_logout_session_deleted.png)

# Authorization - <span style="color: lightgreen;">getting access to some things</span>
