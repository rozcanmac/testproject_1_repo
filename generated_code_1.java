/**
 * The PhysicsCalculator class provides methods for calculating physical properties such as density, mass, and volume.
 */
public class PhysicsCalculator {
    
    /**
     * Calculates the density given mass and volume.
     * @param mass the mass of the object (in appropriate units).
     * @param volume the volume of the object (in appropriate units).
     * @return the calculated density.
     */
    public double calculateDensity(double mass, double volume) {
        return mass / volume;
    }
    
    /**
     * Calculates the mass given density and volume.
     * @param density the density of the object (in appropriate units).
     * @param volume the volume of the object (in appropriate units).
     * @return the calculated mass.
     */
    public double calculateMass(double density, double volume) {
        return density * volume;
    }
    
    /**
     * Calculates the volume given density and mass.
     * @param density the density of the object (in appropriate units).
     * @param mass the mass of the object (in appropriate units).
     * @return the calculated volume.
     */
    public double calculateVolume(double density, double mass) {
        return mass / density;
    }
}