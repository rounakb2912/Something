import streamlit as st
import pandas as pd
import random
import os
from datetime import datetime, date


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Celestial Inn Hotel",
    page_icon="🏨",
    layout="wide"
)


# ============================================================
# FILE NAMES
# ============================================================

CUSTOMER_FILE = "dummy_customers.csv"
ROOM_FILE = "dummy_rooms.csv"
FEEDBACK_FILE = "feedback.txt"


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.hotel-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
}

.hotel-subtitle {
    text-align: center;
    font-size: 20px;
    color: #666666;
}

.room-card {
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #dddddd;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# GENERATE DUMMY CUSTOMER DATA
# ============================================================

def generate_dummy_data(num_records):

    names = [
        "Alice",
        "Bob",
        "Charlie",
        "Diana",
        "Eve",
        "Frank",
        "Grace",
        "Hannah",
        "Ivan",
        "Judy"
    ]

    room_numbers = list(range(101, 401))

    data = []

    for i in range(num_records):

        check_in = datetime.now().date()

        check_out = (
            check_in +
            pd.Timedelta(
                days=random.randint(1, 10)
            )
        )

        data.append({

            "Customer ID": i + 1,

            "Name": random.choice(names),

            "Room Number": random.choice(
                room_numbers
            ),

            "Check-in Date":
                check_in.strftime("%Y-%m-%d"),

            "Check-out Date":
                check_out.strftime("%Y-%m-%d")

        })

    return pd.DataFrame(data)


# ============================================================
# GENERATE DUMMY ROOMS
# ============================================================

def generate_dummy_rooms(num_rooms):

    room_types = [
        "Single",
        "Double",
        "Suite"
    ]

    amenities_list = [

        "Wi-Fi, Breakfast",

        "Wi-Fi",

        "Spa",

        "Wi-Fi, Pool",

        "Wi-Fi, Breakfast, Spa",

        "Wi-Fi, Lunch"

    ]

    data = []

    for i in range(num_rooms):

        room_number = 101 + i

        room_type = random.choice(
            room_types
        )

        price_per_night = random.randint(
            100,
            600
        )

        amenities = random.choice(
            amenities_list
        )

        data.append({

            "Room Number":
                room_number,

            "Room Type":
                room_type,

            "Price per night":
                price_per_night,

            "Status":
                "Available",

            "Amenities":
                amenities

        })

    return pd.DataFrame(data)


# ============================================================
# INITIALIZE DATABASE
# ============================================================

def initialize_data():

    if not os.path.exists(
        CUSTOMER_FILE
    ):

        customers_df = generate_dummy_data(
            300
        )

        customers_df.to_csv(
            CUSTOMER_FILE,
            index=False
        )


    if not os.path.exists(
        ROOM_FILE
    ):

        rooms_df = generate_dummy_rooms(
            300
        )

        rooms_df.to_csv(
            ROOM_FILE,
            index=False
        )


# ============================================================
# LOAD DATA
# ============================================================

def load_customers():

    if os.path.exists(
        CUSTOMER_FILE
    ):

        return pd.read_csv(
            CUSTOMER_FILE
        )

    return pd.DataFrame(
        columns=[
            "Customer ID",
            "Name",
            "Room Number",
            "Check-in Date",
            "Check-out Date"
        ]
    )


def load_rooms():

    if os.path.exists(
        ROOM_FILE
    ):

        return pd.read_csv(
            ROOM_FILE
        )

    return pd.DataFrame(
        columns=[
            "Room Number",
            "Room Type",
            "Price per night",
            "Status",
            "Amenities"
        ]
    )


def save_customers(
    customers_df
):

    customers_df.to_csv(
        CUSTOMER_FILE,
        index=False
    )


def save_rooms(
    rooms_df
):

    rooms_df.to_csv(
        ROOM_FILE,
        index=False
    )


# ============================================================
# INITIALIZE FILES
# ============================================================

initialize_data()


# ============================================================
# LOAD DATA
# ============================================================

customers_df = load_customers()

rooms_df = load_rooms()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="hotel-title">'
    '🏨 Celestial Inn Hotel'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hotel-subtitle">'
    'Where Luxury Meets Comfort'
    '</div>',
    unsafe_allow_html=True
)


st.divider()


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

st.sidebar.title(
    "🏨 Celestial Inn"
)

st.sidebar.write(
    "Hotel Management System"
)

st.sidebar.divider()


menu = st.sidebar.radio(

    "Navigation",

    [

        "🏠 Home",

        "🛏️ Available Rooms",

        "📅 Book a Room",

        "🚪 Check Out",

        "👤 Customer Information",

        "🔎 Search Rooms",

        "💰 Calculate Bill",

        "📊 Total Revenue",

        "💬 Customer Feedback",

        "🔐 Admin Dashboard"

    ]

)


# ============================================================
# HOME
# ============================================================

if menu == "🏠 Home":

    st.header(
        "Welcome to Celestial Inn"
    )

    st.write(
        """
        Welcome to Celestial Inn Hotel, where luxury meets
        comfort in the heart of tranquility!
        """
    )

    st.write(
        """
        Whether you're here for a relaxing retreat,
        a family vacation, or a business trip,
        Celestial Inn provides the perfect blend
        of modern amenities and warm hospitality.
        """
    )


    st.divider()


    # Statistics

    total_rooms = len(
        rooms_df
    )

    available_rooms = len(
        rooms_df[
            rooms_df["Status"]
            == "Available"
        ]
    )

    booked_rooms = len(
        rooms_df[
            rooms_df["Status"]
            == "Booked"
        ]
    )

    total_customers = len(
        customers_df
    )


    col1, col2, col3, col4 = st.columns(4)


    col1.metric(
        "Total Rooms",
        total_rooms
    )


    col2.metric(
        "Available Rooms",
        available_rooms
    )


    col3.metric(
        "Booked Rooms",
        booked_rooms
    )


    col4.metric(
        "Customers",
        total_customers
    )


# ============================================================
# AVAILABLE ROOMS
# ============================================================

elif menu == "🛏️ Available Rooms":

    st.header(
        "🛏️ Available Rooms"
    )


    available_rooms = rooms_df[
        rooms_df["Status"]
        == "Available"
    ]


    if available_rooms.empty:

        st.warning(
            "No available rooms at the moment."
        )

    else:

        st.dataframe(

            available_rooms[

                [

                    "Room Number",

                    "Room Type",

                    "Price per night",

                    "Amenities"

                ]

            ],

            use_container_width=True,

            hide_index=True

        )


# ============================================================
# BOOK ROOM
# ============================================================

elif menu == "📅 Book a Room":

    st.header(
        "📅 Book a Room"
    )


    available_rooms = rooms_df[
        rooms_df["Status"]
        == "Available"
    ]


    if available_rooms.empty:

        st.warning(
            "No rooms are currently available."
        )

    else:

        with st.form(
            "booking_form"
        ):

            customer_name = st.text_input(
                "Customer Name"
            )


            room_number = st.selectbox(

                "Select Room",

                available_rooms[
                    "Room Number"
                ].tolist()

            )


            selected_room = available_rooms[
                available_rooms[
                    "Room Number"
                ]
                == room_number
            ].iloc[0]


            st.info(

                f"Room Type: "
                f"{selected_room['Room Type']}  |  "
                f"Price: ${selected_room['Price per night']} per night  |  "
                f"Amenities: "
                f"{selected_room['Amenities']}"

            )


            check_in = st.date_input(

                "Check-in Date",

                min_value=date.today()

            )


            check_out = st.date_input(

                "Check-out Date",

                min_value=date.today()

            )


            submit = st.form_submit_button(

                "Confirm Booking"

            )


        if submit:

            if not customer_name.strip():

                st.error(
                    "Please enter the customer's name."
                )

            elif check_out <= check_in:

                st.error(
                    "Check-out date must be after "
                    "the check-in date."
                )

            else:

                # Check overlapping bookings

                overlap = customers_df[

                    (

                        customers_df[
                            "Room Number"
                        ]
                        == room_number

                    )

                    &

                    (

                        pd.to_datetime(
                            customers_df[
                                "Check-in Date"
                            ]
                        )
                        < pd.Timestamp(
                            check_out
                        )

                    )

                    &

                    (

                        pd.to_datetime(
                            customers_df[
                                "Check-out Date"
                            ]
                        )
                        > pd.Timestamp(
                            check_in
                        )

                    )

                ]


                if not overlap.empty:

                    st.error(

                        "This room is already "
                        "booked for these dates."

                    )

                else:

                    if customers_df.empty:

                        customer_id = 1

                    else:

                        customer_id = (

                            int(

                                customers_df[
                                    "Customer ID"
                                ].max()

                            )

                            + 1

                        )


                    new_customer = pd.DataFrame({

                        "Customer ID":
                            [customer_id],

                        "Name":
                            [customer_name],

                        "Room Number":
                            [room_number],

                        "Check-in Date":
                            [
                                check_in.strftime(
                                    "%Y-%m-%d"
                                )
                            ],

                        "Check-out Date":
                            [
                                check_out.strftime(
                                    "%Y-%m-%d"
                                )
                            ]

                    })


                    customers_df = pd.concat(

                        [

                            customers_df,

                            new_customer

                        ],

                        ignore_index=True

                    )


                    rooms_df.loc[

                        rooms_df[
                            "Room Number"
                        ]
                        == room_number,

                        "Status"

                    ] = "Booked"


                    save_customers(
                        customers_df
                    )

                    save_rooms(
                        rooms_df
                    )


                    st.success(

                        f"Booking confirmed! "
                        f"Customer ID: {customer_id}"

                    )

                    st.balloons()


# ============================================================
# CHECKOUT
# ============================================================

elif menu == "🚪 Check Out":

    st.header(
        "🚪 Customer Check-Out"
    )


    booked_rooms = rooms_df[
        rooms_df["Status"]
        == "Booked"
    ]


    if booked_rooms.empty:

        st.info(
            "There are currently no booked rooms."
        )

    else:

        room_number = st.selectbox(

            "Select Room",

            booked_rooms[
                "Room Number"
            ].tolist()

        )


        if st.button(
            "Complete Check-Out"
        ):

            rooms_df.loc[

                rooms_df[
                    "Room Number"
                ]
                == room_number,

                "Status"

            ] = "Available"


            save_rooms(
                rooms_df
            )


            st.success(

                f"Room {room_number} "
                "is now available."

            )


# ============================================================
# CUSTOMER INFORMATION
# ============================================================

elif menu == "👤 Customer Information":

    st.header(
        "👤 Customer Information"
    )


    if customers_df.empty:

        st.info(
            "No customer records available."
        )

    else:

        customer_id = st.number_input(

            "Enter Customer ID",

            min_value=1,

            step=1

        )


        if st.button(
            "Search Customer"
        ):

            customer = customers_df[

                customers_df[
                    "Customer ID"
                ]
                == customer_id

            ]


            if customer.empty:

                st.error(
                    "Customer not found."
                )

            else:

                st.dataframe(

                    customer,

                    use_container_width=True,

                    hide_index=True

                )


# ============================================================
# SEARCH ROOMS
# ============================================================

elif menu == "🔎 Search Rooms":

    st.header(
        "🔎 Search Rooms"
    )


    col1, col2 = st.columns(2)


    with col1:

        room_type = st.selectbox(

            "Room Type",

            [

                "Single",

                "Double",

                "Suite"

            ]

        )


    with col2:

        max_price = st.number_input(

            "Maximum Price per Night",

            min_value=0,

            value=600

        )


    filtered_rooms = rooms_df[

        (

            rooms_df[
                "Room Type"
            ]
            == room_type

        )

        &

        (

            rooms_df[
                "Price per night"
            ]
            <= max_price

        )

        &

        (

            rooms_df[
                "Status"
            ]
            == "Available"

        )

    ]


    st.subheader(
        "Search Results"
    )


    if filtered_rooms.empty:

        st.warning(
            "No rooms found matching your criteria."
        )

    else:

        st.dataframe(

            filtered_rooms,

            use_container_width=True,

            hide_index=True

        )


# ============================================================
# CALCULATE BILL
# ============================================================

elif menu == "💰 Calculate Bill":

    st.header(
        "💰 Calculate Customer Bill"
    )


    if customers_df.empty:

        st.info(
            "No customer records available."
        )

    else:

        customer_id = st.number_input(

            "Customer ID",

            min_value=1,

            step=1

        )


        if st.button(
            "Generate Bill"
        ):

            customer = customers_df[

                customers_df[
                    "Customer ID"
                ]
                == customer_id

            ]


            if customer.empty:

                st.error(
                    "Customer not found."
                )

            else:

                customer = customer.iloc[0]


                room_number = customer[
                    "Room Number"
                ]


                room = rooms_df[

                    rooms_df[
                        "Room Number"
                    ]
                    == room_number

                ]


                if room.empty:

                    st.error(
                        "Room information not found."
                    )

                else:

                    room = room.iloc[0]


                    check_in = pd.to_datetime(

                        customer[
                            "Check-in Date"
                        ]

                    )


                    check_out = pd.to_datetime(

                        customer[
                            "Check-out Date"
                        ]

                    )


                    nights = (

                        check_out
                        - check_in

                    ).days


                    price = room[
                        "Price per night"
                    ]


                    total = (
                        nights
                        * price
                    )


                    st.success(
                        "Bill Generated"
                    )


                    col1, col2 = st.columns(2)


                    col1.write(
                        f"**Customer ID:** "
                        f"{customer_id}"
                    )

                    col1.write(
                        f"**Customer Name:** "
                        f"{customer['Name']}"
                    )

                    col1.write(
                        f"**Room Number:** "
                        f"{room_number}"
                    )


                    col2.write(
                        f"**Room Type:** "
                        f"{room['Room Type']}"
                    )

                    col2.write(
                        f"**Number of Nights:** "
                        f"{nights}"
                    )

                    col2.write(
                        f"**Price per Night:** "
                        f"${price}"
                    )


                    st.divider()


                    st.subheader(

                        f"Total Bill: ${total}"

                    )


# ============================================================
# TOTAL REVENUE
# ============================================================

elif menu == "📊 Total Revenue":

    st.header(
        "📊 Total Revenue"
    )


    total = 0


    for _, row in customers_df.iterrows():

        room = rooms_df[

            rooms_df[
                "Room Number"
            ]
            == row[
                "Room Number"
            ]

        ]


        if room.empty:

            continue


        check_in = pd.to_datetime(

            row[
                "Check-in Date"
            ]

        )


        check_out = pd.to_datetime(

            row[
                "Check-out Date"
            ]

        )


        nights = (

            check_out
            - check_in

        ).days


        price = room[
            "Price per night"
        ].values[0]


        total += (
            nights
            * price
        )


    st.metric(

        "Total Revenue",

        f"${total}"

    )


# ============================================================
# CUSTOMER FEEDBACK
# ============================================================

elif menu == "💬 Customer Feedback":

    st.header(
        "💬 Customer Feedback"
    )


    tab1, tab2 = st.tabs(

        [

            "Leave Feedback",

            "View Feedback"

        ]

    )


    with tab1:

        customer_name = st.text_input(

            "Your Name"

        )


        feedback = st.text_area(

            "Your Feedback"

        )


        if st.button(

            "Submit Feedback"

        ):

            if not customer_name.strip():

                st.error(
                    "Please enter your name."
                )

            elif not feedback.strip():

                st.error(
                    "Feedback cannot be empty."
                )

            else:

                with open(

                    FEEDBACK_FILE,

                    "a"

                ) as f:

                    f.write(

                        customer_name
                        + ": "
                        + feedback
                        + "\n"

                    )


                st.success(

                    "Thank you for your feedback!"

                )


    with tab2:

        if os.path.exists(
            FEEDBACK_FILE
        ):

            with open(

                FEEDBACK_FILE,

                "r"

            ) as f:

                feedback_list = f.readlines()


            if feedback_list:

                for feedback in feedback_list:

                    st.write(
                        "💬 " + feedback.strip()
                    )

            else:

                st.info(
                    "No feedback available."
                )

        else:

            st.info(
                "No feedback available."
            )


# ============================================================
# ADMIN DASHBOARD
# ============================================================

elif menu == "🔐 Admin Dashboard":

    st.header(
        "🔐 Admin Dashboard"
    )


    admin_password = st.text_input(

        "Enter Admin Password",

        type="password"

    )


    if admin_password == "admin123":

        st.success(
            "Admin access granted."
        )


        admin_tab1, admin_tab2, admin_tab3 = st.tabs(

            [

                "📅 All Bookings",

                "🏨 Manage Rooms",

                "➕ Add Room"

            ]

        )


        # ----------------------------------------------------
        # ALL BOOKINGS
        # ----------------------------------------------------

        with admin_tab1:

            st.subheader(
                "All Customer Bookings"
            )


            st.dataframe(

                customers_df,

                use_container_width=True,

                hide_index=True

            )


        # ----------------------------------------------------
        # MANAGE ROOMS
        # ----------------------------------------------------

        with admin_tab2:

            st.subheader(
                "Manage Room Status"
            )


            st.dataframe(

                rooms_df,

                use_container_width=True,

                hide_index=True

            )


            room_number = st.number_input(

                "Room Number",

                min_value=101,

                step=1

            )


            new_status = st.selectbox(

                "New Status",

                [

                    "Available",

                    "Booked"

                ]

            )


            if st.button(

                "Update Room Status"

            ):

                if room_number in rooms_df[
                    "Room Number"
                ].values:

                    rooms_df.loc[

                        rooms_df[
                            "Room Number"
                        ]
                        == room_number,

                        "Status"

                    ] = new_status


                    save_rooms(
                        rooms_df
                    )


                    st.success(

                        f"Room {room_number} "
                        f"updated to {new_status}."

                    )

                else:

                    st.error(
                        "Room not found."
                    )


        # ----------------------------------------------------
        # ADD ROOM
        # ----------------------------------------------------

        with admin_tab3:

            st.subheader(
                "➕ Add New Room"
            )


            new_room_number = st.number_input(

                "Room Number",

                min_value=101,

                step=1

            )


            new_room_type = st.selectbox(

                "Room Type",

                [

                    "Single",

                    "Double",

                    "Suite"

                ]

            )


            new_price = st.number_input(

                "Price per Night",

                min_value=1,

                value=100

            )


            new_amenities = st.text_input(

                "Amenities",

                value="Wi-Fi"

            )


            if st.button(

                "Add New Room"

            ):

                if new_room_number in rooms_df[
                    "Room Number"
                ].values:

                    st.error(

                        "This room number "
                        "already exists."

                    )

                else:

                    new_room = pd.DataFrame({

                        "Room Number":
                            [new_room_number],

                        "Room Type":
                            [new_room_type],

                        "Price per night":
                            [new_price],

                        "Status":
                            ["Available"],

                        "Amenities":
                            [new_amenities]

                    })


                    rooms_df = pd.concat(

                        [

                            rooms_df,

                            new_room

                        ],

                        ignore_index=True

                    )


                    save_rooms(
                        rooms_df
                    )


                    st.success(

                        f"Room {new_room_number} "
                        "added successfully."

                    )


    elif admin_password:

        st.error(
            "Incorrect admin password."
        )


# ============================================================
# FOOTER
# ============================================================

st.sidebar.divider()

st.sidebar.caption(
    "Celestial Inn Hotel Management System"
)

st.sidebar.caption(
    "Project Made By Rounak Bhatiya"
)

st.sidebar.caption(
    "Class: 12th Science | Roll No: 12S016"
)