import React, { useState, useEffect } from 'react';

const ProfilePage = () => {
    // Mocked profile and order data
    const [profile, setProfile] = useState({
        name: "John Doe",
        email: "johndoe@example.com",
        bio: "A short bio about John Doe.",
        avatar: "https://via.placeholder.com/150", // Placeholder avatar
    });

    const [orders, setOrders] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {
        // Fetch profile and order data from your backend
        const fetchProfileData = async () => {
            try {
                setLoading(true);
                setError("");
                const profileResponse = await fetch("/api/user/profile");
                const profileData = await profileResponse.json();
                setProfile(profileData);

                const ordersResponse = await fetch("/api/user/orders");
                const ordersData = await ordersResponse.json();
                setOrders(ordersData);
            } catch (err) {
                setError("Failed to load profile or orders. Please try again later.");
            } finally {
                setLoading(false);
            }
        };

        fetchProfileData();
    }, []);

    const handleLogout = () => {
        console.log("User logged out");
    };

    const handleEditProfile = () => {
        console.log("Edite Profile clicked");
    };

    if (loading) {
        return (
            <div className="flex items-center justify-center min-h-screen">
                <p>Loading...</p>
            </div>
        );
    }

    if (error) {
        return (
            <div className="flex items-center justify-center min-h-screen text-red-500">
                <p>{error}</p>
            </div>
        );
    }
    return (
        <div className="container mx-auto p-4">
            <div className="flex flex-col items-center bg-gray-800 text-white rounded-lg p-6 shadow-lg">
                {/* Avatar */}
                <img
                    src={profile.avatar}
                    alt="Profile Avatar"
                    className="w-32 h-32 rounded-full mb-4 border-4 border-gray-300"
                />
                {/* Profile Information */}
                <div className="text-center">
                    <h1 className="text-3xl font-semibold">{profile.name}</h1>
                    <p className="text-gray-400">{profile.email}</p>
                    <p className="mt-4 text-gray-300">{profile.bio}</p>
                </div>
                {/* Edit Profile Button */}
                <button
                    onClick={handleEditProfile}
                    className="mt-6 bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded-lg duration-300"
                >
                    Edit Profile
                </button>
            </div>

            {/* Order History Section */}
            <div className="mt-8 bg-gray-700 text-white p-4 rounded-lg">
                <h2 className="text-2xl font-semibold">Order History</h2>
                {orders.length === 0 ? (
                    <p className="text-gray-400 mt-4">No orders found.</p>
                ) : (
                    <ul className="mt-4 space-y-4">
                        {orders.map(order => (
                            <li key={order.id} className="flex justify-between items-center border-b border-gray-600 py-2">
                                <span>{order.product}</span>
                                <span>{order.status}</span>
                                <span>{order.total}</span>
                            </li>
                        ))}
                    </ul>
                )}
            </div>
            <div className="mt-8 flex justify-between">
                <button
                    onClick={() => (window.location.href = "/")} //navigate to the home page
                    className="bg-green-500 hover:bg-green-600 text-white font-semibold py-2 px-4 rounded-lg duration-300"
                >
                    back to home
                </button>
                <button
                    onClick={handleLogout}
                    className="bg-red-500 hover:bg-red-600 text-white font-semibold py-2 px-4 rounded-lg duration-300"
                >
                    logout
                </button>
            </div>
        </div>
    );
};

export default ProfilePage;
