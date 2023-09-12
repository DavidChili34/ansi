import toml
import yaml

# Читаем данные из config.toml
with open('config.toml', 'r') as toml_file:
    config_data = toml.load(toml_file)

# Создаем инвентарный файл в формате YAML
inventory = {
    'all': {
        'hosts': {
            config_data['sites']['testpartner']['server_ip']['main']: {
                'id': config_data['sites']['testpartner']['id'],
                'server_group': config_data['sites']['testpartner']['server_group'],
                'partner_name': config_data['sites']['testpartner']['partner_name'],
            }
        },
        'children': {
            'mysql_servers': {
                'hosts': {
                    config_data['sites']['testpartner']['db']['host']: {
                        'base': config_data['sites']['testpartner']['db']['base'],
                        'user': config_data['sites']['testpartner']['db']['user'],
                        'password': config_data['sites']['testpartner']['db']['password'],
                    }
                },
                'vars': {
                    'slaves': config_data['sites']['testpartner']['db']['slaves'],
                }
            }
        }
    }
}

# Записываем инвентарный файл в формате YAML
with open('inventory.yml', 'w') as yaml_file:
    yaml.dump(inventory, yaml_file, default_flow_style=False)

print("Инвентарный файл 'inventory.yml' успешно создан.")

