export const retrieveData = async (endpoint, method = "GET", data = null) => {
  const response = await fetch(`http://localhost:3000/${endpoint}`, {
    method,
    data,
  });

  return await response.json();
};
