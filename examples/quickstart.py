
from async_bybit_p2p import P2P
import asyncio


async def main():
    api = P2P(
        testnet=True,
        api_key="x",
        api_secret="x"
    )

    # 1. Get current balance
    print(
        await api.get_current_balance(
            accountType="FUND",
            coin="USDC"
        )
    )

    # 2. Get account information
    print(
        await api.get_account_information()
    )

    # 3. Get ads list
    print(
        await api.get_ads_list()
    )

    # 4. Get ad detail
    print(await api.get_ad_details(
        itemId="1234567890123456789"
    ))

    # 5. Update/reOnline ads
    print(await api.update_ad(
        id="1234567890123456789",
        priceType=1,
        premium=90,  # these values can all be either int or str, library handles it automatically
        price=78.3,
        minAmount=500,
        maxAmount=3500000,
        remark="Contact @kolya5544 on Telegram once you've paid.",
        tradingPreferenceSet={
            "hasUnPostAd": 0,
            "isKyc": 1,
            "isEmail": 0,
            "isMobile": 0,
            "hasRegisterTime": 0,
            "registerTimeThreshold": 0,
            "orderFinishNumberDay30": 0,
            "completeRateDay30": "",
            "nationalLimit": "",
            "hasOrderFinishNumberDay30": 0,
            "hasCompleteRateDay30": 0,
            "hasNationalLimit": 0
        },
        paymentIds=["6558"],  # has to be str
        actionType="MODIFY",  # use ACTIVE to just reactivate the ad
        quantity="25000",
        paymentPeriod="15"
    ))

    # 6. Remove ad
    print(await api.remove_ad(
        itemId="1234567890123456789"
    ))

    # 7. Get Orders
    print(await api.get_orders(
        page=1,
        size=10
    ))

    # 8. Get Pending Orders
    print(await api.get_pending_orders(
        page=1,
        size=10
    ))

    # 9. Get counterparty info
    print(await api.get_counterparty_info(
        originalUid="118027304",
        orderId="1234567890123456789"
    ))

    # 10. Get order details
    print(await api.get_order_details(
        orderId="1234567890123456789"
    ))

    # 11. Release digital asset
    print(await api.release_assets(
        orderId="1234567890123456789"
    ))

    # 12. Mark order as paid
    print(await api.mark_as_paid(
        orderId="1234567890123456789",
        paymentType="123",
        paymentId="5544"
    ))

    # 13. Get chat messages
    print(await api.get_chat_messages(
        orderId="1234567890123456789",
        startMessageId=0,
        size=100
    ))

    # 14. Upload chat file
    print(await api.upload_chat_file(
        upload_file="D:/test.png"
    ))

    # 15. Send chat message
    import uuid
    print(await api.send_chat_message(
        message="Hello, please send funds to the bank account specified",
        contentType="str",
        orderId="1234567890123456789",
        msgUuid=uuid.uuid4().hex
    ))

    # 16. Post new advertisement
    print(await api.post_new_ad(
        tokenId="USDT",
        currencyId="RUB",
        side="1",
        priceType=1,
        premium=90,
        price=78.3,
        minAmount=500,
        maxAmount=3500000,
        remark="Contact @kolya5544 on Telegram once you've paid.",
        tradingPreferenceSet={
                "hasUnPostAd": 0,
                "isKyc": 1,
                "isEmail": 0,
                "isMobile": 0,
                "hasRegisterTime": 0,
                "registerTimeThreshold": 0,
                "orderFinishNumberDay30": 0,
                "completeRateDay30": "",
                "nationalLimit": "",
                "hasOrderFinishNumberDay30": 0,
                "hasCompleteRateDay30": 0,
                "hasNationalLimit": 0
            },
        paymentIds=["6558"],
        quantity="25000",
        paymentPeriod="15",
        itemType="ORIGIN"
    ))

    # 17. Get online advertisements list
    print(await api.get_online_ads(
        tokenId="USDT",
        currencyId="RUB",
        side="0"
    ))

    # 18. Get user payment
    print(
        await api.get_user_payment_types()
    )

    await api.close_session()

asyncio.run(main())