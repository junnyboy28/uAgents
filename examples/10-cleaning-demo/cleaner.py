from protocols.cleaning import cleaning_proto, Availability, Service

from nexus import Agent
from nexus.setup import fund_agent_if_low


cleaner = Agent(
    name="cleaner",
    port=8001,
    seed="cleaner secret seed phrase",
    endpoint="http://127.0.0.1:8001/submit",
)

fund_agent_if_low(cleaner.wallet.address())

print(cleaner.address)

# build the restaurant agent from stock protocols
cleaner.include(cleaning_proto)

availability = Availability(
    address=25,
    max_distance=10,
    time_start=10,
    time_end=18,
    services=[Service.FLOOR, Service.WINDOW, Service.LAUNDRY],
    min_hourly_price=12,
)
MARKUP = 1.1

cleaner._storage.set(  # pylint: disable=protected-access
    "availability", availability.dict()
)
cleaner._storage.set("markup", MARKUP)  # pylint: disable=protected-access

if __name__ == "__main__":
    cleaner.run()
