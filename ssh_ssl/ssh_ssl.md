# SSH

![client_send_public_key_to_server](images/client_send_public_key_to_server.png)

![client_send_data_usual_command](images/client_send_data_usual_command.png)

![server_send_encrypted_data](images/server_send_encrypted_data.png)

![client_decrypt_data](images/client_decrypt_data.png)

# SSL

![ssl_server_and_client_pub_key](images/ssl_server_and_client_pub_key.png)

![sll_server_and_client_crypt_data](images/sll_server_and_client_crypt_data.png)

## Public key encrypts data
## Private key decrypts data


# How to use?

### Generate ssh key to ~/.ssh/

```
ssh-keygen -t ed25519 -C "Gitlab SSH Key"
```

### Add publish ssh key to gitlab

![add_public_key_to_gitlab](images/add_public_key_to_gitlab.png)


### Set ~/.gitconfig
```
git config --global user.name "your_username"
git config --global user.email "your_email_address@example.com"
```