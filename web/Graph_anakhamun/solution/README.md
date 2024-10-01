# Graph Anakhamun Writeup

## Step 1: Directory Discovery

To begin, after exploring the `home` and `maybe` directories, we will need to perform a directory brute-force attack. Using the wordlist `seclists/Discovery/Web-Content/directory-list-2.3-small.txt`, you will discover a `/graph2` directory that reveals a GraphQL interface.

## Step 2: Database Enumeration

We can initiate schema enumeration using the following GraphQL introspection query:

```graphql
{
  __schema {
    types {
      name
      fields {
        name
      }
    }
  }
}

```

This query will reveal the available types in the database, including `User`, `Hints`, and `Secret`. Each type contains fields that may be valuable for further enumeration.

## Step 3: Enumerating Types

### **User Type**:

When querying the `User` type,  we won’t find anything useful.

### **Hints Type**:

The `Hints` type requires an `ID` parameter. To extract all available hints, you need to use tools like **Burp Suite Intruder** or a custom script to cycle through different `ID` values. 

That is the query for the first part of the flag:

**query{hints(id:131){id message}}**

### **Secret Type**:

Accessing the `Secret` type requires a password. In the main `home` page, we will find the first part of the password encoded in Base64. The second part of the password is hidden in the metadata of an image located in the `maybe` directory, can be accessed through a tool like Exiftool .

The query to get the second part of the Flag: 

**query{secret(password:"Yom_Wara_Y0m_7abib1"){hidden}}**
