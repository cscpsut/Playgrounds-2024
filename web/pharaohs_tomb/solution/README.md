## Source code review
The key vulnerability is in the register endpoint. When users register, their form data is processed and directly added to a global users dictionary without any validation or restrictions. This introduces a mass assignment vulnerability, where the application accept any paramter sent by the user, no matter what or how many paramters are they.

## Exploit
By intercepting and modifying the registration request, you can include a role field in the form submission, assigning yourself the role of "pharaoh" or "guard". This allows unauthorized access to the gold (flag) that is otherwise restricted to higher-privilege users.

```
username: intruder
password: password123
confirm_password: password123
role: pharaoh
```

1. Navigate to the registration page and intercept the request (using burpsuite)
2. Add a `role` field with the value pharaoh in the intercepted request.
3. Complete the registration and login as the newly created pharaoh user.
4. Visit the `/gold` endpoint to retrieve the flag.

This can be automated check the [script](./solve.py) 
