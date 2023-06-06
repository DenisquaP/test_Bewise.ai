lin_compose:
	sudo docker compose up -d --build
lin_migrate:
	sudo docker exec task1-app-1 alembic upgrade heads
lin_down:
	sudo docker compose down && sudo docker rmi task1-app

win_compose:
	docker-compose up -d --build
win_migrate:
	docker exec task1-app-1 alembic upgrade heads
win_down:
	docker-compose down && docker rmi task2-app