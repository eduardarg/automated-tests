from caqui import synchronous
from caqui.easy.capabilities import CapabilitiesBuilder, TimeoutsBuilder

driver_url = "http://127.0.0.1:9999"

# Definindo as capabilities
capabilities = (
    CapabilitiesBuilder()
    .browser_name("chrome")  # Defina o nome do navegador (no caso, "chrome")
    .accept_insecure_certs(True)  # Aceitar certificados inseguros
    .timeouts(TimeoutsBuilder().implicit(1).build())  # Defina o tempo de espera implícito
    .additional_capability(
        {"goog:chromeOptions": {"extensions": [], "args": ["--headless"]}}  # Configurações do Chrome (opcional)
    )
).build()

# Estabelecendo a sessão com as capabilities
session = synchronous.get_session(driver_url, capabilities)

try:
    synchronous.get(driver_url, session, "https://www.google.com")
    print("Página carregada com sucesso")
finally:
    synchronous.close_session(driver_url, session)
