import subprocess

def get_whois(domain):
    try:
        result = subprocess.check_output(['whois', domain], universal_newlines=True, stderr=subprocess.STDOUT)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error fetching whois for {domain}: {e.output}"

def main():
    domains = []

    # Read domains from the file
    with open("domains.txt", "r") as file:
        for line in file:
            domains.append(line.strip())

    # Write whois results to the output file
    with open("whois.txt", "w") as output:
        for domain in domains:
            output.write(f"Whois for {domain}:\n")
            output.write("-" * 40 + "\n")
            result = get_whois(domain)
            output.write(result + "\n")
            output.write("=" * 40 + "\n\n")

if __name__ == "__main__":
    main()
