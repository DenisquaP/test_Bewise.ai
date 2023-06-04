lin_compose:
	sudo docker compose up -d
lin_migrate:
	sudo docker exec task2-app-1 alembic upgrade heads
down_lin:
	sudo docker compose down && sudo docker rmi task2-app

win_compose:
	docker-compose up -d
win_migrate:
	docker exec task2-app-1 alembic upgrade heads
down_win:
	docker-compose down && docker rmi task2-app