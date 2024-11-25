# 8.1b Setting up the Environment on Saturn Cloud

<a href="https://www.youtube.com/watch?v=WZCjsyV8hZE&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-8-01b.jpg"></a>

## Links

* [Request access](https://zoomcamp.internal.saturnenterprise.io/)

## Notes

### Setting up the Environment on Saturn Cloud (update for Nov 2024 / macOS 15.1)

1. On website click `Secrets` (1.) -> create `new` (2.)![new Secret](https://github.com/user-attachments/assets/c895d558-b666-4bc7-bf07-ce5a186b4144)

2. In terminal run:

```bash
cat ~/.ssh/id_rsa
```

3. Copy the key and paste it in the secret value field, name it `id_rsa`, add an empty line and a dot `.`, make sure there are no empty characters in the line after `-----END OPENSSH PRIVATE KEY-----`. Click `Add`.
4. Under resources (1.) select `New Python Server` (2.). ![New resource](https://github.com/user-attachments/assets/4bf0748a-ce66-4b53-a993-165f0d38eee9)

5. Configure the server:
   1. give it a name (1.)
   2. Show advanced settings (2.)
   3. select 10Gi (3.)
   4. select GPU (4.)
   5. select TensorFlow environment (5.)
   6. select pip (6.) and add scipy
   7. add your github repo `git:....` (7.) (optional)
   8. allow SSH (8.)
   9. create the server (9.)

![Create Saturn Resource](https://github.com/user-attachments/assets/1e1aad55-0e9b-46a3-922e-bdd291004009)


6. when you added a github repo, you need to set your SSH public key. See yellow warning in image below. Click on the link.

![Needs public key](https://github.com/user-attachments/assets/5d770e99-1299-4e27-ad2d-5ee5014710f2)


7. In terminal run:

```bash
cat ~/.ssh/id_rsa.pub
```

and copy the key. Set name, paste key in the value field and click `Add`.

![Add public key](https://github.com/user-attachments/assets/232b9155-79ab-484a-bc00-d8674c0b39e9)


You can manage your keys under User (1.), manage <username> (2.), SSH keys (3.)

![Manage keys](https://github.com/user-attachments/assets/7d16cfdf-b33f-4cb2-a792-e06f7b3baf2f)


You will find the configured resource at the bottom of the resources page.

>[!CAUTION]
>Your ssh keys could have different names, important is that the private key is named `id_rsa` and the public key is named `id_rsa.pub`. Depending on the crypto system you use, the key could be named `id_rsa` or `id_ed25519` or `id_ecdsa` or `id_dsa`. The public key will have the same name with `.pub` at the end. Never share your private key with anyone.

Add notes from the video (PRs are welcome)

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

## Navigation

* [Machine Learning Zoomcamp course](../)
* [Session 8: Neural Networks and Deep Learning](./)
* Previous: [Fashion classification](01-fashion-classification.md)
* Next: [TensorFlow and Keras](02-tensorflow-keras.md)
