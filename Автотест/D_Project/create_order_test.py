import data
import sender_stand_request


# Успешное создание заказа и получение его по track номеру
def test_create_order_success_response():
    order_body = data.order_body.copy()

    create_response = sender_stand_request.create_new_order(order_body)

    assert create_response.status_code == 201

    new_track = create_response.json()["track"]
    assert new_track != ''

    get_response = sender_stand_request.get_order(new_track)
    assert get_response.status_code == 200
