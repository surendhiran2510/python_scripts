import paramiko

def restart_service(hostname, username, password, service_name):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(hostname, username=username, password=password)
        stdin, stdout, stderr = ssh_client.exec_command(f'sudo service {service_name} restart')
        output = stdout.read().decode('utf-8')
        print(output)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ssh_client.close()

# Example usage
hostname = 'remote_server_ip'
username = 'your_username'
password = 'your_password'
service_name = 'service_to_restart'

restart_service(hostname, username, password, service_name)
