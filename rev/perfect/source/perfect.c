#include <stdio.h>
#include <string.h>
#include <openssl/evp.h>
#include <openssl/sha.h>

void compute_sha256(const char *input, unsigned char output[SHA256_DIGEST_LENGTH]) {
    EVP_MD_CTX *mdctx = EVP_MD_CTX_new();
    const EVP_MD *md = EVP_sha256();

    EVP_DigestInit_ex(mdctx, md, NULL);
    EVP_DigestUpdate(mdctx, input, strlen(input));
    EVP_DigestFinal_ex(mdctx, output, NULL);
    
    EVP_MD_CTX_free(mdctx);
}

void print_hash(unsigned char hash[SHA256_DIGEST_LENGTH]) {
    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
        printf("%02x", hash[i]);
    }
}

int is_prime(long long n) {
    if (n <= 1) return 0;
    if (n <= 3) return 1;
    if (n % 2 == 0 || n % 3 == 0) return 0;
    for (long long i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return 0;
    }
    return 1;
}

int is_perfect(long long number) {
    for (long long p = 2; ; p++) {
        long long mersenne_prime = (1LL << p) - 1;
        if (is_prime(mersenne_prime)) {
            long long perfect_candidate = (1LL << (p - 1)) * mersenne_prime;
            if (perfect_candidate == number) {
                return 1; 
            } else if (perfect_candidate > number) {
                return 0; 
            }
        }
    }
    return 0; 
}

int main() {
    char result[12];
    unsigned char hash[SHA256_DIGEST_LENGTH];
    char hash_prefix[4]; 
    char comparison_string[4] = {'d', '4', '8', '\0'}; 
    long long number; 
    char number_str[20]; 

    printf("Enter a positive number: ");
    scanf("%lld", &number); 

    if (is_perfect(number)) {
        snprintf(number_str, sizeof(number_str), "%lld", number);
        compute_sha256(number_str, hash); 
        snprintf(hash_prefix, sizeof(hash_prefix), "%02x%02x%02x", hash[0], hash[1], hash[2]); 
        if (strcmp(hash_prefix, comparison_string) == 0) {
            printf("Correct!!\nHere is your flag: PlaygroundsCTF{");
            print_hash(hash); 
            printf("}\n");
        } else {
            printf("Nope.\n");
        }
    } else {
        strcpy(result, "Nope.\n");
        printf("%s", result);
    }

    return 0;
}
