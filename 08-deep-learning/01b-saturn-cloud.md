# 8.1b Setting up the Environment on Saturn Cloud

<a href="https://www.youtube.com/watch?v=WZCjsyV8hZE&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-8-01b.jpg"></a>

## Links

* [Request access](https://zoomcamp.internal.saturnenterprise.io/)

## Notes

### Setting up the Environment on Saturn Cloud (update for Nov 2024 / macOS 15.1)

1. On website click `Secrets` (1.) -> create `new` (2.)![new Secret](./images/01_new_secret.png)
2. In terminal run:

```bash
cat ~/.ssh/id_rsa
```

3. Copy the key and paste it in the secret value field, name it `id_rsa`, add an empty line and a dot `.`, make sure there are no empty characters in the line after `-----END OPENSSH PRIVATE KEY-----`. Click `Add`.
4. Under resources (1.) select `New Python Server` (2.). ![New resource](./images/02_new_rescource.png)
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

![Create Saturn Resource](./images/03_saturn_cloud_10Gi_GPU_tensorflow_pip.png)

6. when you added a github repo, you need to set your SSH public key. See yellow warning in image below. Click on the link.

![Needs public key](./images/04_ssh_public_key_needed.png)

7. In terminal run:

```bash
cat ~/.ssh/id_rsa.pub
```

and copy the key. Set name, paste key in the value field and click `Add`.

![Add public key](./images/05_add_public_key.png)

You can manage your keys under User (1.), manage <username> (2.), SSH keys (3.)

![Manage keys](./images/06_git_ssh_keys.png)

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
