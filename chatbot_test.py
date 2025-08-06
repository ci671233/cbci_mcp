from cbci_mcp.client import CBCIMCPClient

client = CBCIMCPClient()
client.start_server()

client.setup(config="config.yaml", questions="questions.yaml", schema="schema.yaml")

answer = client.ask("서울 2023년 학생수")
print(answer)

client.stop_server()